<script>
    import Button from "$lib/Button/Button.svelte";
</script>
<div id="bottom-nav">
    <div id="info"><h1>Rock Club</h1><p>Collecting Rock since never</p></div>
    <Button/>
</div>
<style>
     @import url('https://fonts.googleapis.com/css2?family=Palanquin&display=swap');
    *{
        font-family:'Palanquin', sans-serif;
        margin: 0;
        padding: 0;
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
        opacity: 100%;
        width: 48vw;
        height: 25vh;
        justify-self: start;

    }
</style>