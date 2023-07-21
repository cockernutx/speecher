import type {LayoutLoadEvent} from './$types';

export const prerender = true
export const ssr = false

export async function load(event: LayoutLoadEvent) {
    return {
        options: {
            videoUrl: "",
            selectedLanguage: "Detect Language",
            translate: false,
            initialPrompt: "",
            selectedModel: "medium"
        }
    }
}