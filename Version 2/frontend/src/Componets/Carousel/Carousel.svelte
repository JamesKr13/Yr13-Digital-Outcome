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
    <div class="x"><img src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="stuff">
        <div class="A">
            <div id="bottom-nav">
                <div class="info">
                    <h1>Rock Club</h1>
                    <p>Collecting Rock since never</p>
                </div>
                <Button/>
            </div>
        </div>
    </div>
    <div><img src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="stuff">
        <div class="A">
            <div id="bottom-nav">
                <div class="info">
                    <h1>Rock Club</h1>
                    <p>Collecting Rock since never</p>
                </div>
                <Button/>
            </div>
        </div>
    </div>
    <div><img src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="stuff">
        <div class="A"><div id="bottom-nav">
            <div class="info"><h1>Rock Club</h1><p>Collecting Rock since never</p></div>
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
        background-color: #3C3C3C;
        opacity: 80%;
        width: 48vw;
        height: 25vh;
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
</style>
