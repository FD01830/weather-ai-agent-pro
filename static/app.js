
const c=document.getElementById('chat'),i=document.getElementById('msg');
async function send(){
 const m=i.value.trim(); if(!m)return;
 c.innerHTML+=`<div class="user">${m}</div>`; i.value=""; c.scrollTop=c.scrollHeight;
 c.innerHTML+=`<div class="bot" id="typing">⛅ Thinking...</div>`;
 const r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:m})});
 const j=await r.json();
 document.getElementById('typing').outerHTML=`<div class="bot">🌤️ ${j.response||j.error}</div>`;
 c.scrollTop=c.scrollHeight;
}
document.getElementById('send').onclick=send;
i.addEventListener('keydown',e=>{if(e.key==='Enter')send();});
