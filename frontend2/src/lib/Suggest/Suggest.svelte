<script></script>

<div class="box">
    <div class="suggest">
        <img src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="">
        <div class="text"></div>
    </div>
    <div class="suggest">
        <img src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="">
        <div class="text"></div>
    </div>
    <div class="suggest">
        <img src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="">
        <div class="text"></div>
    </div>
</div>

<style>
    .box {
        width: 100%;
        height: 35vmax;
        /* background-color: red; */
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
    }
    .suggest {
        box-shadow: 0.05vmax 0.05vmax 1vmax #3C3C3C;
        margin-top: auto;
        margin-bottom: auto;
        width: 20vmax;
        height: 23vmax;
        border-radius: 3vmax;
        display: flex;
        flex-direction: column;
    }
    .suggest:hover {
        box-shadow: 0.05vmax 0.05vmax 1vmax #30A8DB;
    }
    img {
        object-fit: cover;
        width: 100%;
        height: 70%;
        border-top-right-radius: 3vmax;
        border-top-left-radius: 3vmax;
    }
    .text {
        background-color: #fff;
        width: 100%;
        height: 40%;
        border-bottom-right-radius: 3vmax;
        border-bottom-left-radius: 3vmax;

    }
</style>