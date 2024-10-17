import {View} from "./base/component.ts";
import {IEvents} from "./base/Events.ts";
import {ensureElement} from "../shared/utils.ts";

const downloadItem = (blob: Blob, fileName: string) => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName;
    a.click();
    window.URL.revokeObjectURL(url);
}



interface IOutputView {
    file: File,
}

export class OutputView extends View<IOutputView> {
    _file: File | null = null;

    handleClickDownload = () => {
        if (this._file) {
            try {
                downloadItem(this._file, this._file.name);
            } catch (e) {
                console.error(e);
            }
            this.events.emit("file-downloaded");
        }
    }

    $: {
        downloadButton: HTMLButtonElement
    }

    constructor(events: IEvents) {
        super(ensureElement("#download-section"), events);

        this.$ = {
            downloadButton: ensureElement<HTMLButtonElement>(".download-button", this.container),
        };
        this.$.downloadButton.addEventListener("click", this.handleClickDownload);
    }

    set file(file: File | null) {
        this.$.downloadButton.disabled = file === null;

        this._file = file;
    }

}
