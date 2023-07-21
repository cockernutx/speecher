<script lang="ts">
	import { languages, models } from './transcriptionData';
	let files: any;

	$: console.log(data.options.videoUrl);

	function fileSelected(event: any) {
		if (event.currentTarget.files && event.currentTarget.files[0]) {
			data.options.videoUrl = URL.createObjectURL(event.currentTarget.files[0]);
		}
	}

	export let data;
</script>

<main>
	<fieldset>
		<legend> Transcription Options </legend>

		<div>
			<label for="language-selection">Select the language: </label>
			<select name="language-selection" bind:value={data.options.selectedLanguage}>
				<option value="Detect Language" selected>Detect Language</option>
				{#each languages as language}
					<option value={language}>{language}</option>
				{/each}
			</select>
		</div>
		<div>
			<label for="model-selection">Select the model: </label>
			<select name="model-selection" bind:value={data.options.selectedModel}>
				{#each models as model}
					<option value={model}>{model}</option>
				{/each}
			</select>
		</div>
		<div>
			<input
				bind:checked={data.options.translate}
				type="checkbox"
				id="translate"
				name="translate"
			/>
			<label for="translate">Translate</label>

			<div />
		</div>
	</fieldset>
	<br />
	<input
		id="file"
		type="file"
		accept="video/mp4,video/mkv, video/x-m4v,video/*"
		on:change={fileSelected}
	/>
	{#if data.options.videoUrl}
		<p>
			<!-- svelte-ignore a11y-media-has-caption -->
			<video controls>
				<source src={data.options.videoUrl} />
			</video>
		</p>
		<a href="/transcription/">Start transcription</a>
	{/if}
</main>
