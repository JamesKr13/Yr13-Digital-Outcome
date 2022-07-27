<script>
    import CarouselInfoBox from "$lib/Info-Box/Carousel-Info-Box.svelte";
</script>


<div id="Box">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Logan_Rock_Treen_closeup.jpg/1200px-Logan_Rock_Treen_closeup.jpg" alt="Carousel Image">
    <div id="foot"><CarouselInfoBox/></div>
</div>

<style>
    #Box {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    #foot {
        margin-top:auto;
    }

    img {
        width: 100vw;
        height: 100vh;
        background-color: red;
        position: absolute;
        object-fit: cover;
        z-index: 0;
        display: flex;
        flex-direction: column;
        
    }
</style>
