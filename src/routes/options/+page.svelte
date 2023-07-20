<script lang="ts">
	let files: any;

</script>
<main>
    <input id="file" type="file" accept="video/mp4,video/mkv, video/x-m4v,video/*" bind:files />
    <div>
        <input type="checkbox" id="translate" name="translate"/>
        <label for="translate">Translated</label>
    </div>

	{#if files && files[0]}
        <p>

            <!-- svelte-ignore a11y-media-has-caption -->
            <video controls>
                <source src={URL.createObjectURL(files[0])} />
            </video>
        </p>
    {/if}
</main>