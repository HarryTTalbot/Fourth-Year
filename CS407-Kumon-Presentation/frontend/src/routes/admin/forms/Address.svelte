<script context="module">
  /**
   * @class Holds the various properties used in the `Address` component.
   * @property {string} lineOne
   * @property {string} lineTwo
   * @property {string} lineThree
   * @property {string} cityTown
   * @property {string} provinceDistrict
   * @property {string} postCode
   * @property {string} country
   */
  export class AddressProps {
    constructor() {
      this.lineOne = "";
      this.lineTwo = "";
      this.lineThree = "";
      this.cityTown = "";
      this.provinceDistrict = "";
      this.postCode = "";
      this.country = "";
    }
  }
</script>

<script>
  import { FormGroup, Input, Label, Row, Col } from "sveltestrap";
  /**
   * The values for this set of input fields.
   * @type {AddressProps}
   */
  export let values = new AddressProps();
</script>

<FormGroup>
  <Label for="lineOne">Address Line 1</Label>
  <Input id="lineOne" type="text" bind:value={values.lineOne} />
</FormGroup>

<FormGroup>
  <Label for="lineTwo">Address Line 2</Label>
  <Input id="lineTwo" type="text" bind:value={values.lineTwo} />
</FormGroup>

<FormGroup>
  <Label for="lineThree">Address Line 3</Label>
  <Input id="lineThree" type="text" bind:value={values.lineThree} />
</FormGroup>

<Row>
  <Col>
    <FormGroup>
      <Label for="cityTown">City/Town</Label>
      <Input id="cityTown" type="text" bind:value={values.cityTown} />
    </FormGroup>
  </Col>

  <Col>
    <FormGroup>
      <Label for="provinceDistrict">County</Label>
      <Input
        id="provinceDistrict"
        type="text"
        bind:value={values.provinceDistrict}
      />
    </FormGroup>
  </Col>
</Row>

<FormGroup>
  <Label for="postCode">Post Code</Label>
  <Input id="postCode" bind:value={values.postCode} />
</FormGroup>

<FormGroup>
  <Label for="country">Country</Label>
  <Input id="country" bind:value={values.country} />
</FormGroup>
