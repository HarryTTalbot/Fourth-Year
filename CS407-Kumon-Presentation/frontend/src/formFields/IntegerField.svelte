<!--
@component
A basic wrapper around an HTML `input` with type `text`, which auto-converts the string value to a JavaScript number.

Exported properties:
- `value`: The external numeric value that corresponds to the input field's string value.
- `pattern`: The numeric pattern to use. By default, this is `[0-9]+` (i.e. only integers).

Events:
- `change(e)`: Emitted when the integer value changes.
  - `e.detail` contains the new integer value.

Usage:

```tsx
<IntegerField id="someId" bind:value={myNumberValue} />
```
-->
<script>
  import { createEventDispatcher } from "svelte";
  import { Input } from "sveltestrap";

  import { clamp } from "../utils";

  /**
   * The ID for this input field.
   * @type {string | null}
   */
  export let id = null;

  /**
   * The numeric value of the input field.
   * @type {number | null}
   */
  export let value = null;

  /**
   * The numeric pattern to use.
   * Defaults to `[0-9]+`.
   * @type {string}
   */
  export let pattern = "[0-9]+";

  /**
   * The minimum accepted value.
   * Defaults to 0.
   * @type {number}
   */
  export let min = 0;

  /**
   * The maximum accepted value.
   * Defaults to `Number.MAX_VALUE`.
   * @type {number}
   */
  export let max = Number.MAX_VALUE;

  const dispatch = createEventDispatcher();
  let internalValue = "";

  const onExternalInput = (newNumber) => {
    if (!newNumber) {
      internalValue = "";
    } else {
      value = clamp(newNumber, min, max);
      internalValue = value.toString();
    }
  };

  const onTextInput = (newText) => {
    newText = newText.replace(/[^0-9]/g, "");

    let newValue;
    if (newText.length === 0) {
      newValue = null;
      internalValue = newText;
    } else {
      newValue = clamp(parseInt(newText), min, max);
      internalValue = newValue.toString();
    }

    if (value === newValue) return;
    value = newValue;
    dispatch("change", value);
  };

  // Subscriptions for syncing the integer and string representations
  $: onExternalInput(value);
  $: onTextInput(internalValue);
</script>

<Input {id} {...$$restProps} type="text" {pattern} bind:value={internalValue} />
