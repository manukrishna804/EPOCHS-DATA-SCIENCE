async function askAI() {

    const question = document.getElementById("question").value;
    const answer = document.getElementById("answer");

    if(question.trim()==""){
        alert("Please enter a question.");
        return;
    }

    answer.innerHTML="Thinking...";

    try{

        const response = await fetch("https://epochs-task10-ai-study-assistant.onrender.com/chat",{

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