<script lang="ts">
	let files: any;

</script>

<main class="container">
	<input id="file" type="file" accept="video/mp4,video/mkv, video/x-m4v,video/*" bind:files />
	{#if files && files[0]}
	<p>
		{files[0]}
		<!-- svelte-ignore a11y-media-has-caption -->
		<video controls>
			<source src={URL.createObjectURL(files[0])} />
		</video>
	</p>
{/if}
</main>

<style>
	.logo.vite:hover {
		filter: drop-shadow(0 0 2em #747bff);
	}

	.logo.svelte:hover {
		filter: drop-shadow(0 0 2em #ff3e00);
	}
</style>
