const fs = require('fs')
const ProgressBar = require('./progress.js');
const basePath = '../zh-tw'
const pb = new ProgressBar('进度', 100);

function getfiles(path){    
    //读取目录下所有目录文件  返回数组
    return fs.readdirSync(path,{encoding:'utf8', withFileTypes:true})
}

function to16Le(){
    let files = getfiles('../zh-tw')
    let length = files.length
    console.log(files)
    // files.forEach((file, idx)=>{
    //     fs.readFile(`${basePath}/${file.name}`,(err, data)=>{
    //         if(!err){
    //             console.log(data)
    //             pb.render({ completed: idx, total: length });
    //         }
    //     })
    // })
}
to16Le()