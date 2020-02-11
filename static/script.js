let lang = "EN";
window.onload=()=> {
	document.querySelectorAll("#lang>button").forEach(e => {
		e.addEventListener("click", ()=>{
			window.location=`/${e.innerHTML}`;
		});
	});
	["inp","len"].map(e=>document.getElementById(e))
		.forEach(x=>x.addEventListener("keypress", (event)=>{
		if(event.code=="Enter"){
			fetch("/input", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({
					value:document.getElementById("inp").value,
					length:document.getElementById("len").value,
					lang:window.location.pathname.replace("/","") || lang
				})
			}).then(e=>e.json())
			.then(e=>{
				document.getElementById("result").innerHTML=e.value;
			}).catch(c=>{
				document.getElementById("result").innerHTML="error";
			});
		}
	}));
}