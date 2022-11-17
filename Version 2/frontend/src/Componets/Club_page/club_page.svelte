<script>
    import JoinClub from "../../../Join-Club/Join-Club.svelte";
</script>


<div class="container">
<img class="mainimg">
<h1 class="club"></h1>
<button class="join_now"><p>Join Now</p></button>>
</div>
<div class="main">
    <div class="textbox"><h1 class="title" >About</h1><p class="textarea">34euwierwf twefuhgieu weugfv ewfue fwvcsagu </p></div>
    <img src="https://img.buzzfeed.com/buzzfeed-static/static/2018-10/2/18/campaign_images/buzzfeed-prod-web-06/15-of-the-weirdest-and-darkest-stock-photos-that--2-21628-1538520564-0_dblbig.jpg" alt="" class="img">
</div>
<div class="middlesection">
<h1 class="title" id="support" >Support Your Club</h1>
<button class="donate-now"><p>Donate Now</p></button>>
</div>
<JoinClub/>
<style>
    * {
        overflow:hidden;
    }
    @import url('https://fonts.googleapis.com/css2?family=Palanquin+Dark:wght@700&display=swap');
    .join_now {
        border:none;
        border-radius: 100em;
        background-color: #30A8DB;
        display: flex;
        z-index:4;
        margin-right: 2vw;
        justify-self: end;
        position: absolute;
        top: 60%;
        left: 60%;
        transform: translate(100%, 100%);
        -ms-transform: translate(-50%, -50%);

    }
   
    .join_now:hover {
        background-color: #4dbae8;
    }
    .join_now:active {
        background-color: hotpink;
    
    }

    p {
        color: white;
        font-family: 'Palanquin Dark', sans-serif;
        font-size: 3vmax;
        margin:2vmax;   
    }
    .club {
        position: absolute;
        top: 40%;
        left:50%;
        text-align: right;
        transform: translate(-50%, -50%);
        font-size: 5vw;
        background-color: rgba(60,60,60,0.9);
        padding: 3vw;
        padding-left: 5vw;
        padding-right: 5vw;
        color: #fff;
        text-decoration: underline;
    }
    .containter {
        position: relative;
    }
     .join {
        border-radius: 10vmax;
    }
    .mainimg {
        width:100vw;
        height: 100vh;
    }
    #support {
        border-bottom: 1vmax solid #2E1C40;
    }
    .main {
        display: flex;
        flex-direction: row;
        padding: 5vmax;
    }
    .textbox {
        margin-left: 5vmax;
    }
    .textbox, .second_box, .img {
        box-shadow: 0.05vmax 0.05vmax 1vmax #3C3C3C;
        width: 40%;
        height: 35vmax;
        margin-right:5vmax;
        background-color: #fff;
        padding:1vmax;
        border-radius: 5vmax;
    }
    .mainimg,.img {
        object-fit: cover !important;
    }
    .textbox .title {
        text-decoration: underline;
    }
    .title {
        font-size: 4vmax;
        text-align: center !important;
        color: #2E1C40;
    }
    .textarea {
        color: #2E1C40;
        font-size: 2vmax;
    }
    .donate-now {
        border:none;
        border-radius: 100em;
        background-color: #30A8DB;
        display: flex;
        z-index:4;
        margin: auto;
    }
    .middlesection {
        width: 50%;
        margin:auto;
    }


</style>