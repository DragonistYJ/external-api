<template>
  <el-container>
    <el-main>
      <el-row>
        输入Domain，以英文换行(\n)、空格( )、逗号(,)、分号(;)隔开
        <el-button type="primary" @click="batchQuery">查询</el-button>
      </el-row>
      <el-row>
        <el-input type="textarea" :rows="8" v-model="inputDomains" placeholder="例如：www.baidu.com;www.baidu.net"/>
      </el-row>
      <el-row>
        <el-col :span="4">
          请选择数据来源
        </el-col>
        <el-col :span="20">
          <el-select v-model="source" placeholder="请选择来源">
            <el-option
                v-for="item in sources"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                :disabled="item.disabled">
            </el-option>
          </el-select>
        </el-col>
      </el-row>
      <el-row>
        结果
      </el-row>
      <el-row>
        <el-table :data="domainResultShowed" stripe>
          <el-table-column prop="domain" label="域名"/>
          <el-table-column label="状态">
            <template v-slot="scope">
              <el-tag :type="scope.row.status === '正确' ? 'success' : 'danger'">
                {{ scope.row.status }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template v-slot="scope">
              <el-button size="mini" v-if="scope.row.status === '错误'"
                         @click="reQuery(scope.row.domain)">
                重查
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-row>
      <el-row>
        <el-pagination
            @size-change="pageSizeChange"
            @current-change="pageCurrentChange"
            :current-page="currentPage"
            :page-sizes="[10, 15, 20, 50]"
            :page-size="100"
            layout="total, sizes, prev, pager, next, jumper"
            :total="queryResults.length">
        </el-pagination>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: "Domain",
  data() {
    return {
      source: "vt",
      sources: [{"value": "vt", "label": "Virus Total", "disabled": false},
        {"value": "qianxin", "label": "奇安信", "disabled": true}],
      currentPage: 1,
      pageSize: 10,
      inputDomains: "",
      queryResults: []
    }
  },
  computed: {
    domainResultShowed: function () {
      let start = (this.currentPage - 1) * this.pageSize;
      return this.queryResults.slice(start, start + this.pageSize);
    },
  },
  methods: {
    batchQuery() {
      this.queryResults = [];
      let domains = this.inputDomains.split(/[ \n,;]/);
      for (let i = 0; i < domains.length; i++) {
        this.$axios.get("/vt/domain?domain=" + domains[i])
            .then(res => {
              if (res.data["state"] === "success") {
                this.queryResults.push({"domain": domains[i], "status": "正确"});
              } else {
                this.queryResults.push({"domain": domains[i], "status": "错误"});
                this.$message({
                  message: domains[i] + " " + res.data["message"],
                  type: 'warning'
                });
              }
            })
            .catch(err => {
              this.$message({
                message: err,
                type: 'error'
              });
              this.queryResults.push({"domain": domains[i], "status": "错误"});
            });
      }
    },
    pageSizeChange(val) {
      this.pageSize = val;
    },
    pageCurrentChange(val) {
      this.currentPage = val;
    },
    reQuery(domain) {
      this.$axios.get("/vt/domain?domain=" + domain)
          .then(res => {
            if (res.data["state"] === "success") {
              let index = this.queryResults.indexOf(domain);
              this.queryResults.splice(index, 0, {"domain": domain, "status": "正确"});
            } else {
              this.$message({
                message: domain + " " + res.data["message"],
                type: 'warning'
              });
            }
          })
          .catch(err => {
            this.$message({
              message: err,
              type: 'error'
            });
          });
    },
  }
}
</script>

<style scoped>
.el-row {
  margin-bottom: 1em;
}
</style>