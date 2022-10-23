<script>
 function logout() {
    alert("Log out")
    document.cookie = "login=false";
    window.location.reload();
 }
 function login() {
    document.cookie = "login=true";
    window.location.reload();
 }
</script>

<div class="Nav" style="margin-top:1vmax;">
    <div class="links"><a href="None">Donation</a></div>
    <div class="links"><a href="None">About</a></div>
    <div class="links"><a href="None">Home</a></div>
    {#if !decodeURIComponent(document.cookie).includes("login=true")}
    <div class="links"><a href="login" on:click={login}>Login</a></div>
    <div class="links"><a href="register">Sign Up</a></div>
    {/if}
</div>
{#if decodeURIComponent(document.cookie).includes("login=true")}
<script>let nav  = document.getElementsByClassName('Nav')[0];
        nav.style.width = '50vmax';
        nav.style.margin.right = '45vmax';</script>
<div class="Login-Nav" href="logout/" style="margin-top:1vmax;">
    <div class="links" href="logout/" on:click={logout}>Sign Out</div>
    <img class="Profile-Pic" src="" alt="Profile">
</div>
{/if}
<style>
    @import url('https://fonts.googleapis.com/css2?family=Palanquin&display=swap');
    * {
        margin-top:1vmax;
        padding: 0;
    }
    .Profile-Pic {
        border-radius: 100vmax;
    }
    .Nav > .links:hover > a, .links {
        color: #30A8DB;
        font-size: 2.2vmax;
        padding-left: 1.6vmax;
        padding-right: 1.6vmax;
    }
    .Login-Nav {
        box-shadow: 0.2vmax 0.2vmax 1vmax #3C3C3C;
        z-index: 1000;
        width: 30vmax;
        height: 5vmax;
        background-color: #30A8DB;;
        display: flex;
        margin:auto;
        border-radius: 8vh;
        z-index: 10;
        text-align: center;
        position: fixed;
        margin-left: 65vmax;
        margin-right: 10vmax;
    }
    .Login-Nav > .links {
        color: whitesmoke;
    }
    .Login-Nav > .links:hover{
        color: black;
        font-size: 2.2vmax;
        padding-left: 1.6vmax;
        padding-right: 1.6vmax;
    }
    .Nav {
        box-shadow: 0.2vmax 0.2vmax 1vmax #3C3C3C;
        z-index: 1000;
        width: 80vmax;
        height: 5vmax;
        background-color: whitesmoke;
        display: flex;
        margin:auto;
        border-radius: 8vh;
        z-index: 10;
        position: fixed;
        margin-left: 10vmax;
        margin-right: 10vmax;
    }
    .links {
        margin:auto
    }
    .links > a, .links{
        text-align: center;
        font-family:'Palanquin', sans-serif;
        font-style: normal;
        font-size: 2vmax;
        padding-left: 2vmax;
        padding-right: 2vmax;
        text-decoration: none;
        flex-direction: row;
        justify-content: center;
        flex-wrap: nowrap;
        color:black;
    }   
    * {
margin: 0;
padding: 0;
}
</style>