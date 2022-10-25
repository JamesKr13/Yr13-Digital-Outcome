<script></script>

<div class="box">
    <div class="suggest">
        <img class="suggest-img" src="" alt="">
        <div class="text"><h1 class="sub-title"></h1><p class="sub-text"></p></div>
    </div>
    <div class="suggest">
        <img class="suggest-img" src="" alt="">
        <div class="text"><h1 class="sub-title"></h1><p class="sub-text"></p></div>
    </div>
    <div class="suggest">
        <img class="suggest-img" src="" alt="">
        <div class="text"><h1 class="sub-title"></h1><p class="sub-text"></p></div>
    </div>
</div>

<style>
    .box {
        padding-top: 5vmax;
        padding-bottom: 5vmax;
        overflow:hidden;
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
        height: 35vmax;
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
        max-height: 60%;
        min-height: 60%;
        border-top-right-radius: 3vmax;
        border-top-left-radius: 3vmax;
    }
    .text {
        overflow:hidden;
        text-align: center;
        background-color: #fff;
        width: 100%;
        height: 40%;
        border-bottom-right-radius: 3vmax;
        border-bottom-left-radius: 3vmax;

    }
    .sub-text {
        overflow:hidden;
    }
    .sub-title {
        font-size: 2vmax;
    }
</style>