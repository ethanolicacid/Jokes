//
//  FeedbackResponseView.swift
//  Jokes
//
//  Created by Ethan Lim on 6/7/22.
//

import SwiftUI

struct FeedbackResponseView: View {
    
    var isPositive: Bool
    
    var body: some View {
        VStack{
            Image(isPositive ? "happy":"sad")
                .resizable()
                .scaledToFit()
                .padding(20)
            Text(isPositive ? "You are an excellent member of society!":"Even plastic waste is better than you")
                .font(.title3)
                .padding()
        }
    }
}

struct FeedbackResponseView_Previews: PreviewProvider {
    static var previews: some View {
        FeedbackResponseView(isPositive: true)
        FeedbackResponseView(isPositive: false)
    }
}
