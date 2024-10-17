import './style.css'
import {InfoView} from "./components/InfoView";
import {EventEmitter} from "./components/base/Events.ts";
import {InputView} from "./components/InputView.ts";
import {OutputView} from "./components/OutputView.ts";
import {parseFile} from "./services/requests.ts";


const events = new EventEmitter();


const infoView = new InfoView(events);
const outputView = new OutputView(events);
const inputView = new InputView(events);

function getCuteDate() {
    const today = new Date();
    return today.toLocaleDateString('en-US', {
      hour: 'numeric',
      minute: 'numeric',
      second: 'numeric',
    });
}

events.on("file-changed", (files: FileList) => {
    console.log("NEW FILE")
    if (files.length > 0) {
        infoView.state = "loading";

        const file = files[0];
        setTimeout(() => parseFile(file).then(response => {
            if (response.ok) {
                infoView.state = "ready";
                const blob = response.blob!;
                outputView.file = new File([blob], `${getCuteDate()}-parsed-${file.name}`);
            } else {
                infoView.error = response.error;
                infoView.state = "error";
            }
        }), 1000)
    }
})


events.on("file-downloaded", () => {
    infoView.state = "complete";

    outputView.file = null;
    inputView.clearInput();
})
