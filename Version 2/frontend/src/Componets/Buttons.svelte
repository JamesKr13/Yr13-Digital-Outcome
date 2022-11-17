<script>
    import { loop_guard } from "svelte/internal";

    export let interest_button;
</script>
<button class="interest_button"><p>I'm Interested</p>
</button>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Palanquin+Dark:wght@700&display=swap');
    button {
        border:none;
        border-radius: 100em;
        background-color: #30A8DB;
        display: flex;
        z-index:4;
        margin-right: 2vw;
        justify-self: end;
;
    }
    button:hover {
        background-color: #4dbae8;
    }
    button:active {
        background-color: hotpink;
    
    }

    p {
        color: white;
        font-family: 'Palanquin Dark', sans-serif;
        font-size: 3vmax;
        margin:2vmax;   
    }
</style>
