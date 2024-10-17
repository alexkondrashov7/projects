/// <reference types="vite/client" />

interface ImportMetaEnv {
    VITE_SERVER_URL: string;
    VITE_CLIENT_URL: string;
    // Add other variables as needed
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}