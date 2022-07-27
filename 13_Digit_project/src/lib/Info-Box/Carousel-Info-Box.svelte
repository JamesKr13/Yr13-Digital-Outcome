<script>
    import Button from "$lib/Button/Button.svelte";
</script>
<div id="bottom-nav">
    <div id="info"> 1234567</div>
    <Button/>
</div>
<style>
    *{
        margin: 0;
        padding: 0;
    }
    #bottom-nav {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
    }

    #info {
        background-color: #3C3C3C;
        opacity: 30%;
        width: 48vw;
        height: 25vh;
        justify-self: start;

    }
</style>