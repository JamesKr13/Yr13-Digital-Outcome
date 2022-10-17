<script src="https://kit.fontawesome.com/447c1c7470.js" crossorigin="anonymous">
import { listen } from "svelte/internal";
import {clickOutside} from "$lib/JS_fn/JS_fn.js"

    let list = [
        {
            name: "Rock Club",
            show: true

        },
        {
            name: "stuff",
            show: true
        }
    ]
    let suggestion = false
    $: search_suggest = suggestion
    
    
    $: suggestions = list.filter(x => x.name)
    function handleClickOutside(event) {
		suggestion=false
	}
</script>
<div class="Text">Discover New</div>
<form>
    <input type="text" placeholder="Search..." id="Search-Bar" on:click="{() => suggestion = true}"/>
    <div>
    <i class="fa-solid fa-magnifying-glass" id="Search">
    </div>
</form>



<style>
    @import url('https://fonts.googleapis.com/css2?family=Palanquin&display=swap');
    
    .Text{
        text-align: center;
        margin-top: 15vmax;
        font-family:'Palanquin', sans-serif;
        font-size: 4vmax;
        border-bottom: solid 1vmax #2E1C40;
        margin-left: 6vmax;
        margin-right: 6vmax;
        font-style:normal;
        color: #2E1C40;
    }
    form, ul {
        display: flex;
        justify-content: center;
        background-color: #E8E8E8;

    } 
    form > * {
        z-index: 1;
    }
    form {
        flex-direction: row;
        margin-top: 10vmax;
    }
    ul {
        flex-direction: column;
    }
    li {
        list-style: none;
        margin-left: auto;
        margin-right: auto;
        
    }
    /* .item {
        width: auto;
    } */
    form > *, ul > * {
        font-family:'Palanquin', sans-serif;
        font-style: normal;
        font-size: 2vmax;
        border-right: none;
        
    }
    li {
        border: solid 0.1vmax #30A8DB;
    }
    ul {
        margin-left: auto;
        margin-right: auto;
        padding: 1vmax;
        border: none;
        width: 75vmax;
        background-color: #fff;
    }

    #Search {
        padding: 6px 10px;
        background-color: #fff;
        cursor: pointer;
        border:none;
        border-bottom-right-radius: 50vmax;
        border-top-right-radius: 50vmax;

    }
    #Search-Bar, .item {
        margin-bottom: 0%;
        padding: 1vmax;
        border: none;
        width: 75vmax;
        box-shadow: none;
        background-color: #fff;
        border-bottom-left-radius: 50vmax;
        border-top-left-radius: 50vmax;

    }
    #Search-Bar:focus{
        outline: none;
        border: 0.1vmax solid #30A8DB;
        border-right: none;
    }

    #Search-Bar:focus + #Search{
        border: 0.1vmax solid #30A8DB;
        box-shadow: #30A8DB;
        border-left: none;
    }
</style>
