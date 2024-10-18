import {View} from "./base/component.ts";
import {IEvents} from "./base/Events.ts";
import {ensureElement} from "../shared/utils.ts";

type State = "waiting" | "ready" | "loading" | "complete" | "error";


interface IInfoView {
    state: State,
    error: string | null,
}


export class InfoView extends View<IInfoView> {
    $: {
        error: HTMLElement,
        subtitle: HTMLElement,
    }

    constructor(events: IEvents) {
        super(ensureElement("#info"), events);

        this.$ = {
            error: ensureElement(".error-message", this.container),
            subtitle: ensureElement(".subtitle", this.container),
        };

        this.state = "waiting";
    }

    set state(state: State) {
        switch (state) {
            case "waiting":
                this.$.subtitle.textContent = "Please upload an image";
                break;
            case "loading":
                this.$.subtitle.textContent = "Loading...";
                break;
            case "ready":
                this.$.subtitle.textContent = "Ready to download";
                break;
            case "complete":
                this.$.subtitle.textContent = "Done! See you later!";
                break;
            case "error":
                this.$.subtitle.textContent = "";
                break;
        }
    }

    set error(message: string | null) {
        this.$.error.textContent = message;
    }
}
