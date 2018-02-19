<template>
  <div :id="symbol" class="chartdiv">
  </div>
</template>

<script>
  import stockController from '@/controllers/Stock.controller'
  import { mapGetters } from 'vuex'

  export default {
    name: 'app',
    props: {
      symbol: {
        type: String
      }
    },
    data() {
      return {
        chart: null,
        displayData: [],
        stockData: []
      }
    },
    computed: {
      ...mapGetters([
        'getStep'
      ])
    },
    watch: {
      getStep: {
        handler(val, oldVal) {
          if(oldVal > val) {
            this.chart.dataSets[0].dataProvider = this.displayData.slice(0, this.displayData.length - val)
            this.chart.validateData()
          } else {
            // getCurrentStep
            stockController.getStockValue(this.symbol, val)
              .then(response => response.stockValue)
              .then(stockValue => {
                this.displayData = this.displayData.concat(stockValue)
                this.chart.dataSets[0].dataProvider = this.displayData
                this.chart.validateData()
              })
          } 
        },
        deep: true
      },
      symbol: {
        handler(val, oldVal) {
          stockController.getStockValue(val, this.getStep)
            .then(response => response.stockValue)
            .then(stockValue => {
              this.displayData = stockValue
              this.chart.dataSets[0].dataProvider = this.displayData
              this.chart.validateData()
            })
        }
      }
    },
    async created() {
      await stockController.getStockValue(this.symbol, this.getStep)
        .then(response => response.stockValue)
        .then(stockValue => {
          this.displayData = stockValue
          this.createChart()
        })
    },
    methods: {
      createChart() {
        this.chart = AmCharts.makeChart(this.symbol, {
          "type": "stock",
          "theme": "light",
          "glueToTheEnd": true,

          "dataSets": [{
            "title": this.symbol,
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
            }, {
              "fromField": "BuyPrice",
              "toField": "buyPrice"
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
              "valueField": "buyPrice",
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