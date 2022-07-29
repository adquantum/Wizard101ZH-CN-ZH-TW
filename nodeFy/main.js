// en -> zh-tw

const translate = require('google-translate-cn-api');
const fs = require('fs')
const readLine = require('readline')
const ProgressBar = require('./progress.js');
const basePath = './new'
const outputPath = '../zh-tw'
let fileName
// 遍历翻译+输出到zh-tw
function tFile(){
    let files = getfiles(basePath)
    files.forEach( async (file, i)=>{
        // console.log(file.name)
        const pb = new ProgressBar('翻译进度', 100);
        fileName = file.name
        let strArr = []
        let lineCount = 0
        let rl = readLine.createInterface({
            input:fs.createReadStream(`${basePath}/${file.name}`,{encoding:'utf16le'})
        })
        rl.on('line', (line)=>{
            // console.log(line.toString('utf16le'))
            // lineStr += `${line.toString('utf16le')}\n`
            strArr[lineCount] = line.toString('utf16le')
            lineCount++
        })
        rl.on('close',()=>{
            // console.log(strArr)
            let p = new RegExp("[`#$&*()={}[]:：/@#&*——{}_]")
            let finished = new Array(strArr.length).fill(false)
            let outArr = []
            var total = strArr.length;
            let index = 0
            let timer
            timer = setInterval(() => {
                try {
                    (function(idx){
                        if(!p.test(strArr[idx]) && strArr[idx] && (idx%3 === 0)){
                            enTotw(strArr[idx].toString('utf16le')).then(text=>{
                                // console.log('翻译：',text)
                                // val = text.toString('utf16le')+'\n'
                                outArr[idx] = text.toString('utf16le')
                                finished[idx] = true
                                // console.log('进度：', (idx/strArr.length).toFixed(2)*100 + '%')
                                pb.render({ completed: idx, total: total-1 });
                                // console.log(outArr[idx])
                                // console.log(finished)
                                if(!finished.includes(false)){
                                    fs.writeFile(`${outputPath}/${file.name}`, outArr.join('\n'),{encoding:'utf16le'}, ()=>{
                                        console.log(file.name,'写入成功')
                                        fs.unlink(`${basePath}/${file.name}`,()=>{})
                                        clearInterval(timer)
                                    })
                                }
                            })
                        }else{
                            // console.log('不翻译:', strArr[idx], idx)
                            if(strArr[[idx]] !== undefined)
                                outArr[idx] = strArr[idx]    
                            finished[idx] = true
                            // console.log(outArr[idx])
                            // console.log(finished)
                            if(!finished.includes(false)){
                                fs.writeFile(`${outputPath}/${file.name}`, outArr.join('\n'),{encoding:'utf16le'}, ()=>{
                                    console.log(file.name,'写入成功--')
                                    fs.unlink(`${basePath}/${file.name}`,()=>{})
                                    clearInterval(timer)
                                })
                            }
                        }
                    })(index)
                } catch (error) {
                 console.log(file.name, 'Google 崩溃')   
                }
                index++
            }, 1000);
        })
    })
}
function getfiles(path){    
    //读取目录下所有目录文件  返回数组
    return fs.readdirSync(path,{encoding:'utf8', withFileTypes:true})
}

function enTotw(str){
    return translate(str, {to: 'zh-tw'}).then(res=>{
        return res.text
    }).catch(err=>console.log(err))
}

tFile()
