//
//  ContentView.swift
//  Flag Raising
//
//  Created by YJ Soon on 21/5/22.
//

import SwiftUI

struct ContentView: View {
    
    @State var counter = 0.0
    
    var body: some View {
        VStack {
            Text("\(counter)")
            
            HStack(alignment: .bottom, spacing: -10) {
                Rectangle()
                    .frame(width: 10)
                Text("🇸🇬")
                    .font(.system(size: 100))
                    .offset(y: -30 * counter)
            }
            
                   
            Button {
                withAnimation {
                    counter = counter + 1
                }
            } label: {
                Text("Raise flag")
                    .padding()
                    .background(.red)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
            
            Button("Reset") {
                withAnimation {
                    counter = 0
                }
            }
            
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
