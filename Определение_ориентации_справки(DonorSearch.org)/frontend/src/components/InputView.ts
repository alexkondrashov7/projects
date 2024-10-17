import {View} from "./base/component.ts";
import {IEvents} from "./base/Events.ts";
import {ensureElement} from "../shared/utils.ts";

interface IInputView {
}


export class InputView extends View<IInputView> {
    $: {
        DropBox: HTMLLabelElement
        InputLabel: HTMLInputElement
    }

    constructor(events: IEvents) {
        super(ensureElement("#upload-section"), events);

        this.$ = {
            DropBox: ensureElement<HTMLLabelElement>(".upload-label", this.container),
            InputLabel: ensureElement<HTMLInputElement>("#file-input", this.container),
        };

        this.$.InputLabel.addEventListener("input", (event) => {
            if (event.target) {
                const files = (event.target as HTMLInputElement).files;
                if (files) {
                    this.events.emit("file-changed", files);
                }
            }
        });
    }

    clearInput() {
        this.$.InputLabel.value = "";
    }
}
