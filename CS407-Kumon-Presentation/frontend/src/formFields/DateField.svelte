<!--
@component
A basic wrapper around an HTML `input` with type `date`, which auto-converts the string value to a JavaScript Date object.
This wrapper is needed for the auto-generated OpenAPI client to work.

See this issue for more details: https://github.com/sveltejs/svelte/issues/3937

Exported properties:
- `date`: The `Date` value that corresponds to the input field's current string value.
- `id`: The ID of the HTML `input` field.

Events:
- `change(e)`: Emitted when the JavaScript date value is changed.
  - `e.detail` contains the new date value.

Usage:

```tsx
<DateField id="someId" bind:date={myDateValue} />
```
-->
<script>
  import dayjs from "dayjs";
  import { createEventDispatcher } from "svelte";
  import { Input } from "sveltestrap";

  const FORMAT = "YYYY-MM-DD";
  const dispatch = createEventDispatcher();

  /**
   * The ID of this input field.
   * @type {string}
   */
  export let id;

  /**
   * The current date value (as a JavaScript Date).
   * @type {Date}
   */
  export let date;

  /**
   * The internal date representation (used for display purposes only).
   * @type {string}
   */
  let internalDate;

  const onExternalInput = (dateValue) => {
    // If the external date was null, set internal date string to empty string
    internalDate = dateValue ? dayjs(dateValue).format(FORMAT) : "";
  };

  const onDateChosen = (dateStr) => {
    // If the internal date string is a valid date, set the external date accordingly
    let tmp = dayjs(dateStr, FORMAT);
    let newDate = tmp.isValid() ? tmp.toDate() : null;

    if (date === newDate) return;
    date = newDate;
    dispatch("change", date);
  };

  // Two subscriptions:
  // - One for updating the displayed date when we set it externally
  // - One for updating the bound date value when we choose a date using the input control
  $: onExternalInput(date);
  $: onDateChosen(internalDate);
</script>

<Input {id} {...$$restProps} type="date" bind:value={internalDate} />
