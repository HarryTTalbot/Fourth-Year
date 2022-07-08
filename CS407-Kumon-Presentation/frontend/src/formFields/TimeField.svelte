<script>
  import dayjs from "dayjs";
  import { createEventDispatcher } from "svelte";
  import { Input } from "sveltestrap";
  const FORMAT = "HH-mm";
  const dispatch = createEventDispatcher();
  /**
   * The ID of this input field.
   * @type {string}
   */
  export let id;
  /**
   * The current date value (as a JavaScript Time).
   * @type {Time}
   */
  export let time;
  /**
   * The internal time representation (used for display purposes only).
   * @type {string}
   */
  let internalTime;
  const onExternalInput = (timeValue) => {
    // If the external time was null, set internal time string to empty string
    internalTime = timeValue ? dayjs(timeValue).format(FORMAT) : "";
  };
  const onTimeChosen = (timeStr) => {
    // If the internal time string is a valid date, set the external time accordingly
    let tmp = dayjs(timeStr, FORMAT);
    let newTime = tmp.isValid() ? tmp.toTime() : null;
    if (time === newTime) return;
    time = newTime;
    dispatch("change", time);
  };
  // Two subscriptions:
  // - One for updating the displayed date when we set it externally
  // - One for updating the bound date value when we choose a date using the input control
  $: onExternalInput(time);
  $: onTimeChosen(internalTime);
</script>

<Input {id} {...$$restProps} type="time" bind:value={internalTime} />
