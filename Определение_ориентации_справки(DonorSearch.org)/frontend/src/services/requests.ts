import {API_URL} from "../app/constants.ts";

interface Response {
    ok: boolean
    error: string | null
    blob: Blob | null
}

export async function parseFile(file: File): Promise<Response> {
    const formData = new FormData();
    formData.append('file', file);

    let blob;

    try {
        console.log(API_URL);
        const response = await fetch(`${API_URL}/predict`, {method: 'POST', body: formData});

        if (response.ok) {
            blob = await response.blob();
        } else {
            return {
                ok: false,
                error: response.statusText,
                blob: null
            }
        }
        return {
            ok: true,
            error: null,
            blob
        }
    } catch (e: any) {
        return {
            ok: false,
            error: e.message,
            blob: null
        }
    }

}