<script lang="ts">
	import { languages, models } from './transcriptionData';
	import {invoke} from '@tauri-apps/api';
	import {goto} from '$app/navigation';
	let files: any;

	$: console.log(data.options.translate);

	function fileSelected(event: any) {
		if (event.currentTarget.files && event.currentTarget.files[0]) {
			data.options.videoUrl = URL.createObjectURL(event.currentTarget.files[0]);
		}
	}

	function startTranscription() {
		invoke('transcribe', {options: data.options});
		goto('/transcription')
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
		<div>
			<input name="initial-prompt" bind:value={data.options.initialPrompt} placeholder="Initial prompt"/> <div class="tooltip">&#8505;<span class="tooltip-text">optional text to provide as a prompt for the first window.</span></div>
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
		<button on:click={startTranscription}>Start transcription</button>
	{/if}
</main>

<style>
	.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black; /* If you want dots under the hoverable text */
}

/* Tooltip text */
.tooltip .tooltip-text {
  visibility: hidden;
  width: 120px;
  background-color: #555;
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;

  /* Position the tooltip text */
  position: absolute;
  z-index: 1;
  bottom: 125%;
  left: 50%;
  margin-left: -60px;

  /* Fade in tooltip */
  opacity: 0;
  transition: opacity 0.3s;
}

/* Tooltip arrow */
.tooltip .tooltip-text::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltip-text {
  visibility: visible;
  opacity: 1;
}
</style>