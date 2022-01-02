const request = require('request')

const url ='https://www.omdbapi.com/?apikey=[......]&s=Batman'

request({url: url, json:true},(error,response)=>{
    var dat = response.body
    console.log(dat)
})