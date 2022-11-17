<script></script>

<div class="box">
    <a class="resultlink" href="/None/">
    <div class="result-1">
        <img class="result-img" src="" alt="">
        <div class="searchtext"><h1 class="result-title"></h1><p class="result-text"></p></div>
    </div>
</a>
<a class="resultlink" href="/None/">
    <div class="result-2">
        <img class="result-img" src="" alt="">
        <div class="searchtext"><h1 class="result-title"></h1><p class="result-text"></p></div>
    </div>
</a>
<a class="resultlink" href="/None/">
    <div class="result-3">
        <img class="result-img" src="" alt="">
        <div class="searchtext"><h1 class="result-title"></h1><p class="result-text"></p></div>
    </div>
</a>
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
    .result-1,.result-2,.result-3 {
        background-color: #fff;
        box-shadow: 0.05vmax 0.05vmax 1vmax #3C3C3C;
        margin-top: auto;
        margin-bottom: auto;
        width: 20vmax;
        height: 35vmax;
        border-radius: 3vmax;
        flex-direction: column;
        display: none;
    }
    .result-1:hover,.result-2:hover,.result-3:hover {
        box-shadow: 0.05vmax 0.05vmax 1vmax #30A8DB;
    }
    /* .result-1 > img,.result-2 > img ,.result > img {
        display: none;
    } */
    img {
        object-fit: cover;
        width: 100%;
        max-height: 60%;
        min-height: 60%;
        border-top-right-radius: 3vmax;
        border-top-left-radius: 3vmax;
    }
    .result-text {
        overflow:hidden;
        text-align: center;
        width: 100%;
        height: 40%;
        border-bottom-right-radius: 3vmax;
        border-bottom-left-radius: 3vmax;

    }
    .result-text {
        overflow:hidden;
    }
    .result-title {
        text-align:center;
        font-size: 2vmax;
    }
</style>