<template>
  <div id="chartdiv">
  </div>
</template>

<script>
  import stockController from '@/controllers/Stock.controller'
  import { mapActions, mapGetters } from 'vuex'

  function sleep() {
    return new Promise(resolve => setTimeout(resolve , 3000))
  }

  export default {
    name: 'app',
    props: {
      stockName: {
        type: String
      }
    },
    data() {
      return {
        chart: null,
        displayData: [],
        stockData: [],
        isChartCreate: false
      }
    },
    computed: {
      ...mapGetters([
        'getStep'
      ])
    },
    watch: {
      getStep: {
        handler(val) {
          if(this.isChartCreate) {
            this.displayData = this.stockData.slice(0, val)
            this.chart.dataSets[0].dataProvider = this.displayData

            this.chart.validateData()
          }
        },
        deep: true
      }
    },
    async created() {
      await this.getStockData(this.stockName)
        .then(response => {
          this.stockData = response
          let step = this.getStep | 1
          
          this.displayData = this.stockData.slice(0, step)
          this.createChart()
          this.isChartCreate = true
          this.$emit("dataChange", this.displayData[this.displayData.length - 1])
        })
    },
    methods: {
      ...mapActions([
        'updateCapital',
        'updatePrice'
      ]),
      async getStockData(stockName) {
        return stockController.getStockData(stockName)
      },
      createChart() {
        this.chart = AmCharts.makeChart("chartdiv", {
          "type": "stock",
          "theme": "light",
          "glueToTheEnd": true,

          "dataSets": [{
            "title": this.stockName,
            "fieldMappings": [{
              "fromField": "Open",
              "toField": "open"
            }, {
              "fromField": "High",
              "toField": "high"
            }, {
              "fromField": "Low",
              "toField": "low"
            }, {
              "fromField": "Close",
              "toField": "close"
            }, {
              "fromField": "Volume",
              "toField": "volume"
            }],
            "compared": false,
            "categoryField": "Date",
            "dataProvider": this.displayData
          }],
          "dataDateFormat": "YYYY-MM-DD",

          "panels": [{
            "title": "Value",
            "percentHeight": 70,

            "stockGraphs": [{
              "type": "candlestick",
              "id": "g1",
              "openField": "open",
              "closeField": "close",
              "highField": "high",
              "lowField": "low",
              "valueField": "close",
              "lineColor": "#0f0",
              "fillColors": "#0f0",
              "negativeLineColor": "#db4c3c",
              "negativeFillColors": "#db4c3c",
              "fillAlphas": 1,
              "comparedGraphLineThickness": 2,
              "columnWidth": 0.7,
              "useDataSetColors": false,
              "balloonText": "open:<b>[[open]]</b><br>close:<b>[[close]]</b><br>low:<b>[[low]]</b><br>high:<b>[[high]]</b>",
              "comparable": true,
              "compareField": "close",
              "showBalloon": true,
              "proCandlesticks": true
            }],

            "stockLegend": {
              "valueTextRegular": undefined,
              "periodValueTextComparing": "[[percents.value.close]]%"
            }

          },

            {
              "title": "Volume",
              "percentHeight": 30,
              "marginTop": 1,
              "showCategoryAxis": false,

              "stockGraphs": [{
                "valueField": "volume",
                "openField": "open",
                "type": "column",
                "showBalloon": false,
                "fillAlphas": 1,
                "lineColor": "#fff",
                "fillColors": "#fff",
                "negativeLineColor": "#db4c3c",
                "negativeFillColors": "#db4c3c",
                "useDataSetColors": false
              }],

              "stockLegend": {
                "markerType": "none",
                "markerSize": 0,
                "labelText": "",
                "periodValueTextRegular": "[[value.close]]"
              },

              "valueAxes": [{
                "usePrefixes": true
              }]
            }
          ],

          "panelsSettings": {
            "plotAreaFillColors": "#333",
            "plotAreaFillAlphas": 1,
            "marginLeft": 76,
            "marginTop": 5,
            "marginBottom": 5
          },

          "chartScrollbarSettings": {
            "graph": "g1",
            "graphType": "line",
            "usePeriod": "WW"
          },

          "valueAxesSettings": {
            "gridColor": "#555",
            "gridAlpha": 1,
            "inside": false,
            "showLastLabel": true
          },

          "balloon": {
            "textAlign": "left",
            "offsetY": 10
          },

          "periodSelector": {
            "position": "bottom",
            "periods": [
              {
                "period": "DD",
                "count": 10,
                "label": "10D"
              }, {
                "period": "MM",
                "count": 1,
                "label": "1M"
              }, {
                "period": "MM",
                "count": 6,
                "label": "6M"
              }, {
                "period": "YYYY",
                "count": 1,
                "label": "1Y"
              },
              {
                "period": "MAX",
                "label": "MAX"
              }
            ]
          }
        })
      }
    }
  }
</script>

<style>
  #chartdiv {
    width: calc(100% - 16px);
    height:calc(50vw * 0.5125);
    margin: 16px 16px 16px 0;
  }
</style>
