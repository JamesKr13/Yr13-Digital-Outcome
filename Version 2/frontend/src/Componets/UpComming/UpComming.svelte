<script src="https://kit.fontawesome.com/447c1c7470.js" crossorigin="anonymous">
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
  
      

<div class="box"> 
    <svelte:component this={Carousel} bind:this={carousel} autoplay
    autoplayDuration={5000}
    pauseOnFocus class="Carousel"
    let:showPrevPage
    let:showNextPage>
    <div slot="prev" on:click={showPrevPage} class="custom-arrow custom-arrow-prev">
        <i class="fa-solid fa-angle-left fa-7x"></i>
        </div>
    <div class="suggest">
        <div class="text"><h1></h1><p></p></div>
        <img class="suggest-img" src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="">
    </div>
    <div class="suggest">
        <div class="text"><h1></h1><p></p></div>
        <img class="suggest-img" src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="">
    </div>
    <div class="suggest">
        <div class="text"><h1></h1><p></p></div>
        <img class="suggest-img" src="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg" alt="">
    </div>
    <div slot="next" on:click={showNextPage} class="custom-arrow custom-arrow-next">
        <i class="fa-solid fa-angle-right fa-7x"></i>
    </div>
    </svelte:component>
    
</div>

<style>
    .Carousel {
        background-color: red;
    }
    .box {
        margin-left:auto;
        margin-right: auto;
        width: 80%;
        height: 35vmax;
        /* background-color: red; */
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        margin-bottom: 7vmax;
        border-radius: 100vmax;
    }
    .suggest {
        box-shadow: 0.05vmax 0.05vmax 1vmax #3C3C3C;
        margin-top: auto;
        margin-bottom: auto;
        width: 80vmax;
        height: 30vmax;
        display: flex;
        flex-direction: row;
        margin-bottom: vmax;
        background-color: #fff;
    }
    .suggest > * {
        margin: auto;
        padding: 1vmax;
        border-radius: 3vmax;
    }
    img {
        object-fit: cover;
        width: 100%;
        height: 90%;
        border-top-right-radius: 3vmax;
        border-top-left-radius: 3vmax;
    }
    .text {
        background-color: #fff;
        min-width: 20vmax;
        max-width: 40vmax;
        max-height: 40%;
        border-bottom-right-radius: 3vmax;
        border-bottom-left-radius: 3vmax;
        

    }
</style>