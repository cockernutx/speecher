use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
#[serde(rename_all="camelCase")]
pub struct TranscriptionOptions {

    selected_language: String,
    translate: bool,
    initial_prompt: String,
    selected_model: String
}

#[tauri::command]
pub fn transcribe(options: TranscriptionOptions) -> String {
    println!("WOOWIE");
    String::from("woowie")
}