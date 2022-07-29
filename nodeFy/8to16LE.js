const fs = require('fs')
const ProgressBar = require('./progress.js');
const basePath = './8to16'
const pb = new ProgressBar('进度', 100);
let jschardet = require('iconv-jschardet');
let iconv = require('iconv-lite');

function getfiles(path){    
    //读取目录下所有目录文件  返回数组
    return fs.readdirSync(path,{encoding:'utf8', withFileTypes:true})
}

function to16Le(){
    let files = getfiles(basePath)
    let length = files.length
    // console.log(files)
    files.forEach((file, idx)=>{
        let content = fs.readFileSync(`${basePath}/${file.name}`)
        let ret = jschardet.detect(content);
        if (ret.encoding == 'UTF-8') {
            console.log(ret.encoding)
            content = content.toString('utf16le')
            fs.writeFile(`./8to16/${file.name}`, iconv.decode(fs.readFileSync(`./8to16/${file.name}`), 'UTF8'), {
                encoding: 'utf16le'
              }, function(err) {
                if (err) {
                  throw err;
                }
            });
        } 
        if(ret.encoding == null){
            console.log(ret.encoding)
            content = content.toString('utf16le')
            // fs.writeFile(`./8to16/${file.name}`, content, {encoding:'utf16le'}, ()=>{
            //     pb.render({ completed: idx, total: length });
            // })
            fs.writeFile(`./8to16/${file.name}`, iconv.decode(fs.readFileSync(`./8to16/${file.name}`), 'utf-16le'), {
                encoding: 'utf16le'
              }, function(err) {
                if (err) {
                  throw err;
                }
              });
        }
    })
}
to16Le()