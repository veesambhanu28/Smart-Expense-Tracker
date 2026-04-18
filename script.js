const words=["Web Developer","Frontend Developer","UI Designer"];
let i=0,j=0,text="",del=false;

function type(){
let el=document.querySelector(".text");
if(!el)return;

if(!del && j<=words[i].length){text=words[i].slice(0,j++);}
else if(del && j>=0){text=words[i].slice(0,j--);}

el.innerHTML=text;

if(j==words[i].length){del=true;setTimeout(type,1000);return;}
if(j==0){del=false;i=(i+1)%words.length;}

setTimeout(type,100);
}
type();