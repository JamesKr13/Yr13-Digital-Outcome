<script src="https://kit.fontawesome.com/447c1c7470.js" crossorigin="anonymous">
    import { onMount } from "svelte";
    import Carousel from "./Componets/Carousel/Carousel.svelte";
    import Navigation from "./Componets/Navigation/Navigation.svelte";
    import SearchBar from "./Componets/Search-Bar/SearchBar.svelte";
    import Suggest from "./Componets/Suggest/Suggest.svelte";
    import UpComming from "./Componets/UpComming/UpComming.svelte";
    import Footer from "./Componets/Footer/Footer.svelte";
    import CarouselInfoBox from "./Componets/Info-Box/Carousel-Info-Box.svelte";
    onMount(async () => {
        let resp = await fetch("home/").then((res) => res.json());
        console.log(resp);
        apimessage = JSON.stringify(resp);
    });
const Pages = {
    home: "home",
    login: "login",
    signup: "signup"
}

</script>
<!-- <div class="Box"> -->
<!-- <Navigation/>
{#if url_type("home")}

<Carousel/>
<SearchBar/>
<Suggest/>
<UpComming/>
{/if}
<Footer/> -->
<!-- </div> -->

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