export const prerender = true
export const ssr = false

export async function load(event) {
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