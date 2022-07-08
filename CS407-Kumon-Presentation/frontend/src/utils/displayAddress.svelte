<script>
  export let address;
</script>

{#if address}
  <p class="spacing">
    {address.lineOne}<br/>
    {#if address.lineTwo}
      {address.lineTwo}<br/>
    {/if}
    {#if address.lineThree}
      {address.lineThree}<br/>
    {/if}
    {#if address.cityTown}
      {address.cityTown}<br/>
    {/if}
    {#if address.provinceDistrict}
      {address.provinceDistrict}<br/>
    {/if}
    {address.postCode}<br/>
    {address.country}<br/>
  <p>
{/if}

<style>
  p.spacing {
  line-height: 1.5;
  }
</style>
