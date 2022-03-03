module.exports = {
    outputDir: "../backend/templates",
    assetsDir: process.env.NODE_ENV === 'production' ? '../static' : 'static',
    devServer: {
        proxy: {
            '/backend': {
                target: 'http://127.0.0.1:5000/',
                changeOrigin: true,
                pathRewrite: {
                    '/backend': '/'
                }
            }
        }
    }
};