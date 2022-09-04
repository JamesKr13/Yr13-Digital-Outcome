<script src="https://kit.fontawesome.com/447c1c7470.js" crossorigin="anonymous">
    import Carousel from '$lib/Carousel/Carousel.svelte';
    import Navigation from '$lib/Navigation/Navigation.svelte';
    import SearchBar from '$lib/Search-Bar/SearchBar.svelte';
    import Footer from '$lib/Footer/Footer.svelte';
    import Suggest from '$lib/Suggest/Suggest.svelte';
    import UpComming from '$lib/UpComming/UpComming.svelte';
</script>
<div class="box">
<Navigation/>    
<Carousel/>
<SearchBar/>
<Suggest/>
<UpComming/>
<Footer/>
</div>
<!-- <div id="fex"></div> -->

<style>
     * {
margin: 0;
padding: 0;
background-color: #E8E8E8;

}
.box {
    background-color: none;
    z-index: 0;
    display: flex;
    flex-direction: column;
}

#fex {
    width:100vw;
    height:100vh;
    z-index: 0;
}


</style>