<template>
  <div id="index">
    <slot></slot>
  </div>
</template>

<style>
  #index {
    margin-left: 16px;
    margin-top: 24px;
    padding-bottom: 8px;
    border-radius: 8px;
    background-color: #fff59d;
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2);
    width: calc(100% - 24px);
    height: auto;
  }
</style>
