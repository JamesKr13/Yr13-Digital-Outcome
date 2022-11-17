<script src="https://kit.fontawesome.com/447c1c7470.js" crossorigin="anonymous">
    import CarouselInfoBox from "../Info-Box/Carousel-Info-Box.svelte";
    import Button from "../Button/Button.svelte";
    import { onMount } from 'svelte';

  let Carousel; // for saving Carousel component class
  let carousel; // for calling methods of the carousel instance
  onMount(async () => {
    const module = await import('svelte-carousel');
    Carousel = module.default;
  });

  const handleNextClick = () => {
    carousel.goToNext()
  }
</script>

<div id="Box">
    <svelte:component this={Carousel} bind:this={carousel} autoplay
    autoplayDuration={5000}
    autoplayProgressVisible
    pauseOnFocus class="Carousel"
    style="width: 100vmax"
    let:loaded
    let:showPrevPage
    let:showNextPage>
    <div slot="prev" on:click={showPrevPage} class="custom-arrow custom-arrow-prev">
        <i />
      </div>
    <div class="x"><img class="carousel-img" src="" alt="stuff">
        <div class="A">
            <div id="bottom-nav">
                <div class="info">
                    
                </div>
                <Button/>
                <h1 class="club"></h1>
            </div>
        </div>
    </div>
    <div><img class="carousel-img" src="" alt="stuff">
        <div class="A">
            <div id="bottom-nav">
                <div class="info">

                </div>
                <Button/>
                <h1 class="club"></h1>
            </div>
        </div>
    </div>
    <div><img class="carousel-img" src="" alt="stuff">
        <div class="A"><div id="bottom-nav">
            <div class="info">
               
            </div>
            <h1 class="club"></h1>
            <Button/></div></div></div>
    <div slot="next" on:click={showNextPage} class="custom-arrow custom-arrow-next">
        <i />
      </div>
    </svelte:component>
    
    
    <div id="foot"></div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Palanquin&display=swap');
    .A{
        margin-top: 75vh;
        width: 100%;
        min-height: 100vh;
        position: absolute;
    }
    * {
        font-family:'Palanquin', sans-serif;
        /* margin: 0;
        padding: 0; */
        color: #fff;
    }
    #bottom-nav {   
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
    }

    #info {
        position: absolute;
        background-color: #3C3C3C;
        display: none;
        opacity: 80%;
        width: 48vw;
        height: 25vh;
        z-index: 300;
        justify-self: flex-end;

    }
    .x {
        display: flex;
        min-height: 100vh;    
        min-width:100vw;
        flex-direction: column;
    }
    /* #Box {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    } */
    #foot {
        margin-top:auto;
    }
    img {
        object-fit: cover;
        width: 100vw;
        height: 100vh;
        position: absolute;
    }

    /* img {
        width: 100vw;
        height: 100vh;
        background-color: red;
        position: absolute;
        object-fit: cover;
        z-index: 0;
        display: flex;
        flex-direction: column;
        
    } */
    .club {
        position: absolute;
        top: 10%;
        margin-top: -20vmax;
        left:50%;
        text-align: right;
        z-index:1000;
        transform: translate(-50%, -50%);
        font-size: 5vw;
        background-color: rgba(60,60,60,0.9);
        padding: 3vw;
        padding-left: 5vw;
        padding-right: 5vw;
        width:auto;
        color: #fff;
        text-decoration: underline;
    }
</style>
