<script>

    export let join ;
</script>
<div class="Join">
    <h1 class="join">Join:</h1>
    <p class="messege">Send a messege of your interest to this Club</p>
    <div class="join_space">
        <ul class="entries">
            <li class="type">First Name:</li>
            <li class="type">Last Name:</li>
            <li class="type">Email:</li>
        </ul>
        <ul class="user_inputs">
            <input type="text" class="inputs"><input type="text" class="inputs"><input type="text" class="inputs">
        </ul>
        <button class="go">Submit</button>
        <!-- <div class="first_name">
            <p id="first_name">First Name:</p>
            <textarea name="" id="" cols="30" rows="1" class="entername"></textarea>
        </div>
        <div class="last_name">
            <p id="last_name">Last Name:</p>
            <textarea name="" id="" cols="30" rows="1" class="entername"></textarea>
        </div>
        <div class="email">
            <div id="email">Email:</div>
            <textarea name="" id="" cols="30" rows="1" class="email_enter"></textarea>
        </div> -->
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Chivo&family=Palanquin+Dark:wght@700&display=swap');
    .Join {
        width:80%;
        height: 60%;
        margin:auto;
        background-color: #fff;
        padding: 2vmax;
        border-radius: 5vmax;
        margin-bottom: 7vmax;
        margin-top:5vmax;
    }
    .go {
        border:none;
        border-radius: 100em;
        width: auto;
        height: 4vw;
        background-color: #30A8DB;
        z-index:4;
        margin: auto;
        color: #fff !important;
        display: block;
        font-size: 2vw;
        margin-left:1vw;
    }
    * {
        
        color: #2E1C40;
    }
    .join, .messege {
        font-family: 'Palanquin Dark', sans-serif;
        font-size: 4vmax;
    }
    .join {
        margin-bottom: -3vmax;
    }
    .type {
        font-family: 'Chivo', sans-serif;
        font-size:4vh;
        /* margin-bottom: 4vh; */
    }
    .join_space {
        display:flex;
        flex-direction: row;
    }
    ul {
        list-style-type: none;
    }
    .user_inputs {
        display: flex;
        flex-direction: column;
    }
    .inputs{
        font-family: 'Chivo', sans-serif;
        border-radius: 50vmax;
        min-width: 30vmax;
        background-color: #E8E8E8;
        border:none;
    }


</style>