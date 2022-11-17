<script src="https://kit.fontawesome.com/447c1c7470.js" crossorigin="anonymous">
    import Carousel from "./Componets/Carousel/Carousel.svelte";
    import Navigation from "./Componets/Navigation/Navigation.svelte";
    import SearchBar from "./Componets/Search-Bar/SearchBar.svelte";
    import Suggest from "./Componets/Suggest/Suggest.svelte";
    import UpComming from "./Componets/UpComming/UpComming.svelte";
    import Footer from "./Componets/Footer/Footer.svelte";
    import CarouselInfoBox from "./Componets/Info-Box/Carousel-Info-Box.svelte";
    import ClubPage from "./Componets/Club_page/club_page.svelte";
    import LoadingDot from "./Componets/LoadingDots/LoadingDot.svelte";
    import Results from "./Componets/Results/Results.svelte";
</script>
<!-- <div class="Box"> -->
<Navigation/>
{#if window.location.href.includes("home")}
<Carousel/>
<SearchBar/>
<LoadingDot/>
<div class="results-1" id="one"><Results/></div>
<div class="results-2" id="two"><Results/></div>
<div class="results-3" id="three"><Results/></div>
<Suggest/>
<UpComming/>
{/if}
{#if window.location.href.includes("club")}
<ClubPage/>
{/if}
<Footer/>
<!-- </div> -->

<style>
     * {
margin: 0;
padding: 0;
background-color: #E8E8E8;

}
.results-1,.results-2,.results-3 {
    display: none;
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