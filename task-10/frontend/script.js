async function askAI() {

    const question = document.getElementById("question").value;
    const answer = document.getElementById("answer");

    if(question.trim()==""){
        alert("Please enter a question.");
        return;
    }

    answer.innerHTML="Thinking...";

    try{

        const response = await fetch("http://127.0.0.1:8000/chat",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                message:question
            })

        });

        const data=await response.json();

        answer.innerHTML=data.response;

    }

    catch(error){

        answer.innerHTML="Error connecting to backend.";

    }

}
function clearChat(){

    document.getElementById("question").value="";
    document.getElementById("answer").innerHTML="Your answer will appear here...";

} function copyAnswer(){

    const text=document.getElementById("answer").innerText;

    navigator.clipboard.writeText(text);

    alert("Response copied!");

}