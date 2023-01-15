library(shinydashboard)
library(shiny)
library(terra)
library(sf)         
library(raster)     
library(spData)        
library(spDataLarge)
library(tidyverse)



greece<-st_read("GRC_ADM2.shp")
poleis<-read_sf("poleis.shp")
raster<-rast("grcRaster.tif")
poleis<-st_transform(poleis,crs(raster))
elevation = terra::extract(raster, vect((poleis)))
pointsHeight = cbind(poleis, elevation)
sf::sf_use_s2(FALSE)
pH<-st_as_sf(pointsHeight)
gr<-st_as_sf(greece)
elevationByState = raster::extract(x = raster, y = vect(greece), df = TRUE) 

summarized<-group_by(elevationByState, ID) %>% 
    summarize_at(vars(raster), list( ~mean(.), ~sd(.)))
gr<-gr%>%mutate(mean=summarized$mean,sd=summarized$sd)



ui <- fluidPage(

    dashboardHeader(title = "GIS Web App"),
    dashboardSidebar(),

    dashboardBody(
        sidebarPanel(
            sliderInput("City",
                        "Height of city",
                        min = 0,
                        max = max(pointsHeight$raster),
                        value = 100),
            sliderInput("Mean",
                        "Mean Height of State",
                        min = 0,
                        max =1200,
                        value = (max(gr$mean)-min(gr$mean))/3),
            sliderInput("sd",
                        "Standard Deviation Height of State",
                        min = 0,
                        max = 570,
                        value = (max(gr$sd)-min(gr$sd))/3)
        ),

        
        mainPanel(
           plotOutput("distPlot")
        )
    )
)


server <- function(input, output) {


    output$distPlot <- renderPlot({
        plot(x=gr%>%filter(gr$mean>=input$Mean & gr$sd>=input$sd)%>%select(geometry),col=rgb(red=0,green=0,blue=0,alpha = 0.2));plot(x=pH%>%filter(pH$raster>=input$City)%>%select(geometry),pch = 17,col=rgb(red=1,green=0,blue=0),add=TRUE)
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
