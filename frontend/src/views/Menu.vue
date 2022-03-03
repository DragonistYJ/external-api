<template>
  <el-row>
    <el-table :data="abilities" style="width: 100%">
      <el-table-column label="功能" width="200">
        <template v-slot="scope">
          <span>{{ scope.row.ability }}</span>
        </template>
      </el-table-column>
      <el-table-column label="来源" width="200">
        <template v-slot="scope">
          <span>{{ scope.row.source }}</span>
        </template>
      </el-table-column>
      <el-table-column label="描述">
        <template v-slot="scope">
          <span>{{ scope.row.description }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="200">
        <template v-slot="scope">
          <el-button size="mini" @click="toAbility(scope.row.target)">
            进入
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-row>
</template>

<script>
export default {
  name: "Menu",
  data() {
    return {
      abilities: [{
        'ability': 'Domain',
        "source": "Virus Total/奇安信",
        'description': '搜集Domain相关信息',
        'target': 'domain'
      }, {
        'ability': 'IP',
        "source": "Virus Total/奇安信",
        'description': '搜集IP地址相关信息',
        'target': 'ip'
      }, {
        'ability': 'URL',
        "source": "Virus Total/奇安信",
        'description': '搜集URL地址相关信息',
        'target': 'url'
      }]
    }
  },
  methods: {
    toAbility(target) {
      this.$router.push(target);
    }
  }
}
</script>

<style scoped>

</style>