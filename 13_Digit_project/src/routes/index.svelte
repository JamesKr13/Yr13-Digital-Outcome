<script>
    import Carousel from '$lib/Carousel/Carousel.svelte';
    import Navigation from '$lib/Navigation/Navigation.svelte';
    import SearchBar from '$lib/Search-Bar/SearchBar.svelte';
</script>
<Navigation/>    
<Carousel/>
<SearchBar/>
<div id="fex"></div>

<style>
     * {
margin: 0;
padding: 0;
background-color: #E8E8E8;

}

#fex {
    width:100vw;
    height:100vh;
    z-index: 0;
}


</style>