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
    <div class="links"><a href="/home/">Home</a></div>
    {#if decodeURIComponent(document.cookie).includes("login=false")}
    <div class="links"><a href="/accounts/login/" on:click={login}>Login</a></div>
    <div class="links"><a href="/register/">Sign Up</a></div>
    {/if}
</div>
{#if decodeURIComponent(document.cookie).includes("login=true")}
<script>let nav  = document.getElementsByClassName('Nav')[0];
        nav.style.width = '50vmax';
        nav.style.margin.right = '45vmax';</script>
<div class="Login-Nav" style="margin-top:1vmax;">
    <div class="dropdown-content">
        <a class="dropdown_item" href="/accounts/logout">logout</a>
        <a class="dropdown_item" href="/Create-Club/">Create A Club</a>
        <a  class="dropdown_item" href="dropdown_item">Delete Account</a>
      </div>
    <!-- <div class="links" href="/accounts/logout">Sign Out</div> -->
    <div class="user-info">
    <div class="username">Nobody</div>
    <div class="email">No Email Found</div></div>
    <img class="Profile-Pic" src="../media/pics/ANNO_PROFILE.png" alt="Profile">
</div>
{/if}
<style>
    @import url('https://fonts.googleapis.com/css2?family=Palanquin&display=swap');
    * {
        margin-top:1vmax;
        padding: 0;
    }
    .email {
        text-align: right;
    }
    .user-info {
        width: 10vmax;
        height: 3vmax;
        margin:1vmax;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-left: auto;
        margin-right: 6vmax;
        text-align: right;
    }
    .Profile-Pic {
        border-radius: 100vmax;
        width: 5vmax;
        height: 5vmax;
        /* border: solid 0.4vmax #fff; */
        position: fixed;
        margin-left: 25vmax;
    }
    .Nav > .links:hover > a, .links {
        color: #30A8DB;
        font-size: 2.2vmax;
        padding-left: 1.6vmax;
        padding-right: 1.6vmax;
    }
    .dropdown-content {
        
        max-width: 20vmax;
        margin-top: 5vmax;
        margin-left: 5vmax;
        display: none;
        flex-direction: column;
        position: absolute;
        /* border-left: solid 0.5vmax #30A8DB;
        border-right: solid 0.5vmax #30A8DB;
        border-bottom: solid 0.5vmax #30A8DB; */
        width: 20vmax;
        height: 10vmax;
        /* border-bottom-left-radius: 4vmax;
        border-bottom-right-radius: 4vmax; */

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
    .dropdown_item {
        background-color: #fff;
        padding: 1vmax;
        /* /* height: 3vmax; */
        display: inline-block;
        text-align: right;
        margin-right: 1vmax;
        /* position: fixed; */
    }
    .Login-Nav:hover .dropdown-content  {
        display: flex;
        
    }
    .dropdown_item:hover  {
        background-color: #30A8DB;
        color: #fff;
    }
    /* .Login-Nav > .links {
        color: whitesmoke;
    }
    .Login-Nav > .links:hover{
        color: black;
        font-size: 2.2vmax;
        padding-left: 1.6vmax;
        padding-right: 1.6vmax;
    } */
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